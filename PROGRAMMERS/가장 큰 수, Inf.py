# max_val = float('inf')
# if max_val > 100000000000000:
#     print(True)
# else:
#     print(False)
#
# #  inf 앞에 minus 붙이면 최소값 생성 가능
# min_val = float('-inf')
# if min_val < -10000000000000000000:
#     print(True)
# else:
#     print(False)

user = User.objects.create_user(request.POST['username'],password = request.POST['password'])
auth.login(request, user)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate