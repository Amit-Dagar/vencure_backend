from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from account.serializers import VendorSignupSerializer, User
from helper import helper


# Create vendor
# post
# params - name, email, password
# /api/vendor/createVendor
class CreateVendor(CreateAPIView):
    permission_classes = [helper.permission.IsAdmin]
    serializer_class = VendorSignupSerializer

    def post(self, request):
        helper.check_parameters(request.data, ['name', 'email', 'password'])

        if User.objects.filter(email=request.data['email']).count() > 0:
            raise helper.exception.NotAcceptable(
                helper.message.USER_EMAIL_EXISTS)

        user = self.get_serializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()

        return helper.createResponse(helper.message.VENDOR_CREATED)
