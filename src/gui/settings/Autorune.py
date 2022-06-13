import tkinter as tk
from src.gui.interfaces import LabelFrame, Frame
from src.common.interfaces import Configurable


class Autorune(LabelFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'Autorune', **kwargs)

        self.Arune_settings = AruneSettings('autorune')
        self.auto_rune = tk.BooleanVar(value=self.Arune_settings.get('Auto-Rune'))


        AR_row = Frame(self)
        AR_row.pack(side=tk.TOP, fill='x', expand=True, pady=5, padx=5)
        check = tk.Checkbutton(
            AR_row,
            variable=self.auto_rune,
            text='Auto-Rune',
            command=self._on_change
        )
        check.pack()


    def _on_change(self):
        self.Arune_settings.set('Autorune', self.auto_rune.get())
        self.Arune_settings.save_config()


class AruneSettings(Configurable):
    DEFAULT_CONFIG = {
        'Auto-Rune': True,
    }

    def get(self, key):
        return self.config[key]

    def set(self, key, value):
        assert key in self.config
        self.config[key] = value
