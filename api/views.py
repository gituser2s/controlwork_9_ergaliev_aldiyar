from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import PhotoSerializer
from photos.models.photo import Photo


class PhotoCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        serializer = PhotoSerializer(data=data)
        data['author'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        photos = Photo.objects.all().exclude(is_deleted=True)
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PhotoDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        photo = Photo.objects.all().exclude(is_deleted=True)
        serializer = PhotoSerializer(photo[kwargs['pk']-1], many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PhotoUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        photo = Photo.objects.get(pk=pk)
        serializer = PhotoSerializer(photo, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotoDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        photo = Photo.objects.get(pk=pk)
        photo.delete()
        return Response(f"Удалено фото: {photo.id}", status=status.HTTP_204_NO_CONTENT)


class FavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        photo = Photo.objects.get(pk=pk)
        user = request.user
        if user in photo.favorite.all():
            photo.favorite.remove(user)
            photo.save()
            return Response({'detail': 'Фото убрано с избранного!'})
        else:
            photo.favorite.add(user)
            photo.save()
            return Response({'detail': 'Фото добавлено в избранное!'})
