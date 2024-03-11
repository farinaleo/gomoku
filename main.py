from ft_gomoku import SettingsStruct

settings = SettingsStruct()
settings.load()
settings.print()
settings.set_fps(20)
settings.save()
