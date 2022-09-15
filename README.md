
# CNN para Clasificación de Imágenes

Web app desarrollada en Django para clasificar imágenes implementando el algoritmo CNN, mediante el entrenamiento de un set de datos tomado de [Kaggle](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset). Puede acceder a la app desde este enlace: https://cnn-django-pytorch.azurewebsites.net

## Tecnologías
- [Django](https://www.djangoproject.com)
- [PyTorch](https://pytorch.org)
- [Bootstrap](https://getbootstrap.com)
- [Docker](https://www.docker.com)
- [Azure](https://www.azure.com/free)
- [GitHub Actions](https://github.com/features/actions)

## Desarrollo
El backend fue programado en Django, usando Python 3.9. Para el frontend no se usó un framework específico para el frontend, pero se añadieron estilos a la plantilla de Django gracias a Bootstrap 4.

Para facilitar el proceso de despliegue, se creó un contenedor en Docker.
## Entrenamiento del modelo
Para entrenar el modelo se utilizó PyTorch con el dataset [Vegetable Image Dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset) de Kaggle, que está compuesto por un total de 21000 imágenes de vegetales, distribuidas en 15 clases. Las imágenes del dataset se dividen en un 70% para entrenamiento, 15% para testing y 15% para validación.

Una vez entrenado, el modelo se exportó a un archivo .pth localizado en la carpeta cnn_classification/data/

El notebook con el código utilizado para entrenar el modelo puede consultarse [aquí](https://colab.research.google.com/drive/10szvpkg4N_-WeXvmad1vU2uh56-4QhZ6?usp=sharing).

## Despliegue
La aplicación se desplego usando los servicios gratuitos de Azure.

En primer lugar, se creó un contenedor local con Docker y se subió a Azure mediante el servicio [Container Registry](https://azure.microsoft.com/es-es/products/container-registry/). Posteriormente, se usó el servicio [App Service](https://azure.microsoft.com/es-es/services/app-service/) para generar una app web a partir del contenedor subido anteriormente. 

Una vez desplegada la app, se configuró CI/CD con GitHub Actions desde las opciones de App Service, con el fin de actualizar y desplegar el contenedor automáticamente cada vez que se registra un commit a la rama master de este repositorio.
