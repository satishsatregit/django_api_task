from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import userSerializer, likeSerializer, BlogPostSerializer
from .models import BlogPost,like,user


class GenericgetAPIView(APIView):
    def get(self,request,id,table_name):
        specific_id =  request.GET.get('id', None)
        table_name = request.GET.get("table_name",None)
        try:
            if table_name=="user":
                data = user.objects.get(user_ID = specific_id)
            elif table_name=="BlogPost":
                data = BlogPost.objects.get(post_id = specific_id)
                user_data = user.objects.get(user_ID = data["user_ID"])
                post = BlogPost.objects.get(post_id=specific_id, user=user_data["user_ID"])

                like_count = like.objects.filter(post=post).count()
                data["likes"]=like_count
            elif table_name=="like":
                data = like.objects.get(like_id = specific_id)

            return Response(data, status=201)
        except :
            return Response(status=400)

class GenericpostAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        if 'table' not in data:
            return Response({"error": "Table name not provided"}, status=400)

        if data['table'] == 'user':
            serializer = userSerializer(data=data)
        elif data['table'] == 'like':
            serializer = likeSerializer(data=data)
        elif data['table'] == 'log':
            serializer = BlogPostSerializer(data=data)
        else:
            return Response({"error": "Invalid table name"}, status=400)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

class GenericputAPIView(APIView):
    def put(self,request,specific_id,table_name,*args, **kwargs):
        updated_data = request.data()
        try:
            try:
                if table_name == "user":
                    data = user.objects.get(user_ID=specific_id)
                elif table_name == "BlogPost":
                    data = BlogPost.objects.get(post_id=specific_id)
                elif table_name == "like":
                    data = like.objects.get(like_id=specific_id)
                return Response(data, status=201)
            except:
                return Response(status=400)
            if updated_data:
                if data['table'] == 'user':
                    serializer = userSerializer(data=data)
                elif data['table'] == 'like':
                    serializer = likeSerializer(data=data)
                elif data['table'] == 'log':
                    serializer = BlogPostSerializer(data=data)
                else:
                    return Response({"error": "Invalid table name"}, status=400)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=201)
        except:
            return Response(serializer.errors, status=400)

class GenericdeleteAPIView(APIView):
    def delete(self, request,specific_id,table_name, *args, **kwargs):
        if table_name == 'User':
            try:
                user_delete_data = user.objects.get(pk = specific_id)
                user_delete_data.delete()
                return Response({"message": "User deleted successfully"}, status=200)
            except user.DoesNotExist:
                return Response({"error": "User not found"}, status=404)

        elif table_name == 'Like':
            try:
                like_delete_data = like.objects.get(pk= specific_id)
                like_delete_data.delete()
                return Response({"message": "Like deleted successfully"}, status=200)
            except like.DoesNotExist:
                return Response({"error": "Like not found"}, status=404)

        elif table_name == 'BlogPost':
            try:
                blogpost_delete_data = BlogPost.objects.get(pk= specific_id)
                blogpost_delete_data.delete()
                return Response({"message": "Blog deleted successfully"}, status=200)
            except BlogPost.DoesNotExist:
                return Response({"error": "BlogPost not found"}, status=404)

        else:
            return Response({"error": "Invalid table name"}, status=400)
