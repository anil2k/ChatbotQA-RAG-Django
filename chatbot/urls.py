# chatbot/urls.py
from django.urls import path
# from .views import EmployeeListCreateAPIView, LeaveRequestListCreateAPIView,ChatbotAPIView, ChatbotQAAPIView
from .views import ChatbotQAAPIView

urlpatterns = [
    # path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    # path('leave-requests/', LeaveRequestListCreateAPIView.as_view(), name='leave-request-list-create'),
    # path('api/chatbot/', ChatbotAPIView.as_view(), name='chatbot_api'),
    path('api/query/', ChatbotQAAPIView.as_view(), name='query'),

    # Add other paths as needed
]
