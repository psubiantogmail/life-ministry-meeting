import anvil.server

@anvil.server.callable
def get_epub(language):
  site = 'https://www.jw.org/id/perpustakaan/jw-lembar-pelajaran/'
  
  if language == 'English':
    site = 'https://www.jw.org/en/library/jw-meeting-workbook/'

  

  
  return 1

