
        btn_silent.bind(on_press=self.toggle_silent)

        btn_medical = Button(
            text="View Medical Info",
            font_size=18
        )
        btn_medical.bind(on_press=self.show_medical_info)

        root.add_widget(title)
        root.add_widget(self.status)
        root.add_widget(btn_emergency)
        root.add_widget(btn_silent)
        root.add_widget(btn_medical)

       
        Clock.schedule_interval(self.check_battery, 10)

        return root

    

    def start_emergency(self, instance):
        self.status.text = "Emergency triggered! Cancel if accidental..."
        self.cancel_time = 5
        Clock.schedule_interval(self.cancel_countdown, 1)

        if not self.silent_mode:
            self.start_siren()

    