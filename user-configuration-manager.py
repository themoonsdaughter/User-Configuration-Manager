test_settings = {'theme' : 'dark', 'volume' : 'on'}
def add_setting (setting , adjustement):
      key = adjustement[0].lower()
      value = adjustement[1].lower()
      if key in setting:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
      else:
        new_setting = setting.update({key : value})
        return f"Setting '{key}' added with value '{value}' successfully!" 
add_setting (test_settings , ('Language','English'))   

def update_setting (setting, adjustement): 
  key = adjustement[0].lower()
  value = adjustement[1].lower()
  if key in setting:
    new_setting = setting.update({key : value})
    return f"Setting '{key}' updated to '{value}' successfully!"
  else:
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
  
update_setting(test_settings , ('volume' , 'off'))

def delete_setting (setting , adjustement):
  adjustement = adjustement.lower()
  if adjustement in setting:
    new_setting = setting.pop(adjustement)
    return f"Setting '{adjustement}' deleted successfully!"
  else:
    return "Setting not found!"

delete_setting(test_settings, 'theme')

def view_settings(setting):
  if len(setting) == 0:
    return "No settings available."
  else:
    result = "Current User Settings:\n"
    for key, value in setting.items():
      key = key.title()
      result = result + f"{key}: {value}\n"
    return result

view_settings(test_settings)