from ._anvil_designer import StartseiteTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    kurse = anvil.server.call("Get_Startseite_Data")

    self.repeating_panel_kurse.items = [
      {
        "kurs_KID": k[0],
        "kurs_Bezeichnung": k[1],
        "kurs_Wochentag": k[2],
        "kurs_Uhrzeit": k[3],
        "trainer_Name": k[4],
        "kurs_Teilnehmer": f"{k[5]}/{k[6]}"
      }
      for k in kurse
    ]

    # Any code you write here will run before the form opens.
