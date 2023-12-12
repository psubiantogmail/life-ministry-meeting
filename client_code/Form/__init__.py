from ._anvil_designer import FormTemplate
from anvil import *
import anvil.server

class Form(FormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    language_list = ['Indonesian', 'English']
    self.drop_down_language.items = language_list