from ._anvil_designer import MitgliederTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Mitglieder(MitgliederTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # Zugriff auf die übergebenen Daten
    self.selected_kid = properties.get("selected_kid", None)
    

  @handle("repeating_panel_mitglieder", "show")
  def repeating_panel_mitglieder_show(self, **event_args):
    """This method is called when the repeating panel is shown on the screen"""
    mitglieder = anvil.server.call('get_verfuegbare_mitglieder', self.selected_kid)
    self.repeating_panel_mitglieder.items = [
      {
        "Mitglied_column": f"{m[1]} {m[2]}"
      }
      for m in mitglieder
    ]


    