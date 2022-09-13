import base64
import io
import os
import torch

from django.shortcuts import render
from torchvision import transforms
from PIL import Image

from .CNN import CNN
from .forms import ImageUploadForm

model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
'cnn_classification/data/trained_model.pth')

model_file = torch.load(model_path, map_location=torch.device('cpu'))

model = CNN(num_classes = 15)
model.load_state_dict(model_file)
model.eval()

classes = ['Frijol', 'Melón_Amargo', 'Porongo', 'Berenjena', 'Brócoli', 'Lechuga', 'Pimentón', 'Zanahoria', 'Coliflor', 'Pepino', 'Papaya', 'Papa', 'Auyama', 'Rábano', 'Tomate']

def transform(image_bytes):
    transformer = transforms.Compose([
        transforms.Resize((150, 150)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.5, 0.5, 0.5],
                            [0.5, 0.5, 0.5])
    ])
    image = Image.open(io.BytesIO(image_bytes))
    return transformer(image).unsqueeze(0)

def prediction(image_bytes):
    tensor = transform(image_bytes)
    output = model(tensor)
    index = output.data.numpy().argmax()
    return classes[index]

def index(request):
    image_uri = None
    predicted_label = None

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():            
            image = form.cleaned_data['imagen']
            image_bytes = image.file.read()    
            encoded_img = base64.b64encode(image_bytes).decode('ascii')
            image_uri = 'data:%s;base64,%s' % ('image/jpeg', encoded_img)

            try:
                predicted_label = prediction(image_bytes)
            except RuntimeError as e:
                print(e)
    else:
        form = ImageUploadForm()

    context = {
        'form': form,
        'image_uri': image_uri,
        'predicted_label': predicted_label,
    }
    return render(request, 'cnn_classification/index.html', context)
