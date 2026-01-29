btn_emergency = Button(
            text="EMERGENCY CALL",
            font_size=26,
            background_color=(1, 0, 0, 1)
        )
        btn_emergency.bind(on_press=self.start_emergency)

        btn_silent = Button(
            text="Silent Mode",
            font_size=18
        )
        btn_silent.bind(on_press=self.toggle_silent)

        btn_medical = Button(
            text="View Medical Info",
            font_size=18