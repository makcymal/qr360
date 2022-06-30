from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions

from .models import DemoQR, QRModel
from .serializers import DemoQRSerializer, QRModelSerializer
from .tasks import update_url


class QRList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            qrs = QRModel.objects.filter(qruser=request.user)
            return Response({
                'success': True,
                'qrs': QRModelSerializer(qrs, many=True).data
            })
        except:
            return Response({'success': False, 'error': 'cant get qrs'})

    def post(self, request):
        serializer = QRModelSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save(qruser=request.user)
                return Response({'success': True, 'qr': serializer.data})
            except:
                return Response({'success': False, 'error': 'cant save qr'})

        return Response({'success': False, 'error': 'data is not valid'})


class QRDetail(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, qr_id):
        try:
            qr = QRModel.objects.filter(qruser=request.user).get(pk=qr_id)
            return Response({
                'success': True,
                'qr': QRModelSerializer(qr).data
            })
        except:
            return Response({'success': False, 'error': 'cant get qr'})

    def put(self, request, qr_id):
        try:
            qr = QRModel.objects.filter(qruser=request.user).get(pk=qr_id)
        except:
            return Response({'success': False, 'error': 'cant get qr'})

        try:
            timer = request.data['timer']
            request.data.pop('timer')
        except:
            pass
        
        serializer = QRModelSerializer(qr, data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
                qr.refresh_from_db()
                
                try:
                    update_url.apply_async((qr.id, qr.next_url_time), countdown=int(timer))
                except:
                    pass
                
                return Response({'success': True, 'qr': serializer.data})
            except:
                return Response({'success': False, 'error': 'cant save qr'})
        
        return Response({'success': False, 'error': 'data is not valid'})

    def delete(self, request, qr_id):
        try:
            qr = QRModel.objects.filter(qruser=request.user).get(pk=qr_id)
        except:
            return Response({'success': False, 'error': 'cant get qr'})

        try:
            qr.image.delete(save=True)
            qr.delete()
            return Response({'success': True})
        except:
            return Response({'success': False, 'error': 'cant delete qr'})


class DemoQRManage(APIView):

    def post(self, request):
        serializer = DemoQRSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'success': True, 'qr': serializer.data})
            except:
                return Response({'success': False, 'error': 'cant save qr'})

        return Response({'success': False, 'error': 'data is not valid'})


class DemoQRManageDetail(APIView):

    def get(self, request, qr_id):
        try:
            qr = DemoQR.objects.get(pk=qr_id)
            return Response({
                'success': True,
                'qr': DemoQRSerializer(qr).data,
            })
        except:
            return Response({'success': False, 'error': 'cant get qr'})

    def put(self, request, qr_id):
        try:
            qr = DemoQR.objects.get(pk=qr_id)
        except:
            return Response({'success': False, 'error': 'cant get qr'})

        serializer = DemoQRSerializer(qr, data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'success': True, 'qr': serializer.data})
            except:
                return Response({'success': False, 'error': 'cant save qr'})

        return Response({'success': False, 'error': 'data is not valid'})
