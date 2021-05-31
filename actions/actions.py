# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# class ActionTrabajoScrumMaster(Action):

#     '''
#         Esta acción muestra las funciones que realiza el Scrum Master en la etapa o evento que solicite el usuario, de no especificar ninguna muestra sus funciones en todas las etapas.
#     '''

#     def name(self) -> Text:
#         return "action_trabajo_scrum_master"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         etapa = tracker.get_slot('etapa')
#         switcher = {
#             'None' : "El Scrum Master es el responsable de que Scrum sea entendido y bien aplicado dentro de la organización.",
#             'planning' : "El Scrum Master asegura que el evento se lleve a cabo y que los asistentes comprendan su propósito.",
#             'review' : "Asegurar que el evento ocurre y que cumple los tiempos establecidos, además de asegurar una colaboración de todo el equipo.",
#             'sprint' : "Guiar al equipo de desarrollo a ser autoorganizado y multifuncional."
#             'backlog': ""
#         }
#         message = switcher.get(etapa)
#         dispatcher.utter_message(message)
#         return [SlotSet('etapa', 'None')]