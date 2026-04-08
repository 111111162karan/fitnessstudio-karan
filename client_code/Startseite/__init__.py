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
    self.repeating_panel_kurse.set_event_handler(
      "x-row-action",
      self.kurs_ausgewaehlt
    )
    # Any code you write here will run before the form opens.

  @handle("repeating_panel_kurse", "show")
  def repeating_panel_kurse_show(self, **event_args):
    """This method is called when the repeating panel is shown on the screen"""
    kurse = anvil.server.call("Get_Startseite_Data")
    print(kurse)

    self.repeating_panel_kurse.items = [
      {
        "Kurs_column": k[0],
        "Wochentag_column": k[1],
        "Uhrzeit_column": k[2],
        "Trainer_column": f"{k[3]} {k[4]}",
        "Teilnehmer_column": k[5]

      }
      for k in kurse
    ]

    
  def kurs_ausgewaehlt(self, kid, **event_args):
    self.selected_kid = kid
    open_form('Startseite.Mitglieder', selected_kid = self.selected_kid)


    