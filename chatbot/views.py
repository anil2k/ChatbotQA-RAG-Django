from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, LeaveRequest
from .serializers import EmployeeSerializer, LeaveRequestSerializer
import joblib
from sklearn.feature_extraction.text import CountVectorizer


from .data.response_data import utter_responses
from .data.entity_detection_cohere import get_cohere_response, process_cohere_response
from .data.intent_detection_cohere import get_cohere_intent, process_cohere_intent
from .data.dialogue_policy_rule import get_actions_for_intent
from .data.custom_action import fetch_leave_balance
from .data import custom_action
from .data.intent_embd import get_intent
from .data import query_data

class ChatbotQAAPIView(APIView):
    def post(self, request, format=None):
        user_message = request.data.get('message')

        query_text=user_message
        response = query_data.generate_response(query_text)

        # Send response back to frontend
        return Response({'message': response})
        