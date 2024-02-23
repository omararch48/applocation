from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from apps.users.models import User
from apps.vehicles.models import Vehicle
from .serializers import VehicleSerializer


@api_view(['GET'])
def get_vehicle(request, pk=None):
    # Auth
    username = request.headers.get('username')
    password = request.headers.get('password')
    user_id = int(request.headers.get('user-id'))
    user = authenticate(username=username, password=password)
    if not user or user.id != user_id:
        return Response(
            {'message': 'Authentication failed'}, status.HTTP_404_NOT_FOUND
        )
    # Get vehicle
    try:
        vehicle = Vehicle.objects.get(id=pk, user=user)
        vehicle_response = VehicleSerializer(vehicle)
    except Vehicle.DoesNotExist:
        return Response(
            {'message': 'Vehicle does not exists'}, status.HTTP_404_NOT_FOUND
        )
    return Response(vehicle_response.data, status.HTTP_200_OK)


@api_view(['POST'])
def create_vehicle(request):
    # Auth
    username = request.data['username']
    password = request.data['password']
    user_id = int(request.data['user_id'])
    user = authenticate(username=username, password=password)
    if not user or user.id != user_id:
        return Response(
            {'message': 'Authentication failed'}, status.HTTP_404_NOT_FOUND
        )
    # Post vehicle
    try:
        user = User.objects.get(id=int(request.data['user']))
        plates=request.data['plates']
        last_position=request.data['last_position']
    except KeyError:
        return Response(
            {'message': 'Missing required fields'}, status.HTTP_400_BAD_REQUEST
        )
    except User.DoesNotExist:
        return Response(
            {'message': 'User does not exist'}, status.HTTP_404_NOT_FOUND
        )
    if not plates:
        return Response(
            {'message': 'Plates not valid'}, status.HTTP_404_NOT_FOUND
        )
    if type(last_position) == str:
        last_position = eval(last_position)
    if not isinstance(last_position, dict) or \
        set(last_position.keys()) != {'lat', 'lng'}:
        return Response(
            {'message': 'Invalid last_position format. \
Must be a dictionary with keys lat and lng'},
            status.HTTP_400_BAD_REQUEST
        )
    vehicle_instance = Vehicle.objects.create(
        user=user,
        plates=plates,
        last_position=last_position,
    )
    vehicle_response = VehicleSerializer(vehicle_instance)
    return Response(vehicle_response.data, status.HTTP_201_CREATED)


@api_view(['GET'])
def get_all_vehicles(request):
    # Auth
    username = request.headers.get('username')
    password = request.headers.get('password')
    user_id = int(request.headers.get('user-id'))
    user = authenticate(username=username, password=password)
    if not user or user.id != user_id:
        return Response(
            {'message': 'Authentication failed'}, status.HTTP_404_NOT_FOUND
        )
    # Get all vehicles by user
    vehicles = Vehicle.objects.filter(user=user)
    vehicles_response = VehicleSerializer(vehicles, many=True)
    return Response(vehicles_response.data, status.HTTP_200_OK)


@api_view(['PATCH', 'PUT'])
def update_vehicle(request, pk=None):
    # Auth
    username = request.data['username']
    password = request.data['password']
    user_id = int(request.data['user_id'])
    user = authenticate(username=username, password=password)
    if not user or user.id != user_id:
        return Response(
            {'message': 'Authentication failed'}, status.HTTP_404_NOT_FOUND
        )
    # Update vehicle
    try:
        vehicle = Vehicle.objects.get(id=pk, user=user)
    except Vehicle.DoesNotExist:
        return Response(
            {'message': 'Vehicle does not exist'}, status.HTTP_404_NOT_FOUND
        )
    if 'user' in request.data:
        try:
            user = User.objects.get(id=int(request.data['user']))
            vehicle.user = user
        except:
            return Response(
                {'message': 'User does not exist'}, status.HTTP_404_NOT_FOUND
            )
    if 'plates' in request.data:
        vehicle.plates = request.data['plates']
    if 'last_position' in request.data:
        last_position = request.data['last_position']
        if type(last_position) == str:
            last_position = eval(last_position)
        vehicle.last_position = last_position
    vehicle.save()
    vehicle_serializer = VehicleSerializer(vehicle)
    message = f'Vehicle with id: {vehicle.id} and plates: \
{vehicle.plates} updated successfully'
    return Response(
        {'message': message, 'vehicle': vehicle_serializer.data},
        status.HTTP_200_OK
    )


@api_view(['DELETE'])
def delete_vehicle(request, pk=None):
    # Auth
    username = request.headers.get('username')
    password = request.headers.get('password')
    user_id = int(request.headers.get('user-id'))
    user = authenticate(username=username, password=password)
    if not user or user.id != user_id:
        return Response(
            {'message': 'Authentication failed'}, status.HTTP_404_NOT_FOUND
        )
    # Delete vehicle
    try:
        vehicle = Vehicle.objects.get(id=pk, user=user)
    except:
        return Response(
            {'message': 'Vehicle does not exists'}, status.HTTP_404_NOT_FOUND
        )
    message = f'Vehicle with id: {vehicle.id} and plates: \
{vehicle.plates} deleted successfully'
    vehicle.delete()
    return Response(
        {'message': message}, status.HTTP_204_NO_CONTENT
    )