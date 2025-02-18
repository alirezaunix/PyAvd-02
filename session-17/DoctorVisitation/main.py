import flet as ft
import jdatetime
from datetime import datetime

file_path = "/Users/alireza/Desktop/pyadv-02/session-17/DoctorVisitation/visitors.txt"
class Visitor:
    def __init__(self, first_name, last_name, age, code, gender, phone, married, reservation_time=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.code = code
        self.gender = gender
        self.phone = phone
        self.married = married
        self.reservation_time = reservation_time

    def to_string(self):
        """Convert visitor data to a comma-separated string."""
        married_str = "Married" if self.married else "Single"
        reservation_str = self.reservation_time.isoformat(
        ) if self.reservation_time else "None"
        return f"{self.first_name},{self.last_name},{self.age},{self.code},{self.gender},{self.phone},{married_str},{reservation_str}"

    @classmethod
    def from_string(cls, data_str):
        """Create a Visitor object from a comma-separated string."""
        fields = data_str.strip().split(",")
        first_name = fields[0]
        last_name = fields[1]
        age = fields[2]
        code = fields[3]
        gender = fields[4]
        phone = fields[5]
        married = fields[6] == "Married"
        reservation_time = datetime.fromisoformat(
            fields[7]) if fields[7] != "None" else None
        return cls(first_name, last_name, age, code, gender, phone, married, reservation_time)


class FileHandler:
    @staticmethod
    def writeIO(filename, data):
        with open(filename, "w") as file:
            for visitor in data:
                file.write(visitor.to_string() + "\n")

    @staticmethod
    def readIO(filename):
        visitors = []
        try:
            with open(filename, "r") as file:
                for line in file:
                    visitors.append(Visitor.from_string(line))
        except FileNotFoundError:
            pass  # If the file doesn't exist, return an empty list
        return visitors


def main(page: ft.Page):
    page.title = "Doctor Reservation App"
    page.theme_mode=ft.ThemeMode.LIGHT
    page.window.width=990
    visitors = []

    visitors = FileHandler.readIO(file_path)

    def add_visitor(e):
        first_name = first_name_input.value
        last_name = last_name_input.value
        age = age_input.value
        code = code_input.value
        gender = gender_dropdown.value
        phone = phone_input.value
        married = married_checkbox.value
        reservation_time = None 
        
        first_name_input.value=""
        last_name_input.value=""
        age_input.value=""
        code_input.value=""
        gender_dropdown.value=""
        phone_input.value=""
        married_checkbox.value=""

        visitor = Visitor(first_name, last_name, age, code,
                          gender, phone, married, reservation_time)
        visitors.append(visitor)
        FileHandler.writeIO(file_path, visitors)
        page.update()

    def make_reservation(e):
        last_name = last_name_reservation_dropdown.value
        selected_date = f"{year_dropdown.value}-{month_dropdown.value}-{day_dropdown.value}"
        selected_time = f"{hour_dropdown.value}:{minute_dropdown.value}"
        reservation_time_str = f"{selected_date} {selected_time}"

        try:
            # Convert Jalali date string to jdatetime object
            jalali_date = jdatetime.datetime.strptime(
                reservation_time_str, "%Y-%m-%d %H:%M")
            # Convert jdatetime to Gregorian datetime for sorting
            gregorian_date = jalali_date.togregorian()
        except ValueError:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Invalid date or time!"))
            page.snack_bar.open = True
            return

        last_name_reservation_dropdown.value=""
        year_dropdown.value=""
        month_dropdown.value=""
        day_dropdown.value=""
        hour_dropdown.value=""
        minute_dropdown.value=""
        page.update()


        for visitor in visitors:
            if visitor.last_name == last_name:
                visitor.reservation_time = gregorian_date
                break

        FileHandler.writeIO(file_path, visitors)
        update_visitor_list()
        page.update()

    def update_visitor_list():
        sorted_visitors = sorted(
            visitors, key=lambda x: x.reservation_time if x.reservation_time else datetime.min)
        visitor_list.controls.clear()
        for visitor in sorted_visitors:
            if visitor.reservation_time:
                jalali_reservation_time = jdatetime.datetime.fromgregorian(
                    datetime=visitor.reservation_time)
                reservation_time_str = jalali_reservation_time.strftime(
                    "%Y-%m-%d %H:%M")
            else:
                reservation_time_str = "No reservation"

            visitor_list.controls.append(
                ft.ListTile(
                    title=ft.Text(
                        f"{visitor.first_name} {visitor.last_name}", color=ft.colors.WHITE),
                    subtitle=ft.Text(
                        f"Reservation Time: {reservation_time_str}", color=ft.colors.WHITE),
                )
            )
        page.update()

    first_name_input = ft.TextField(
        label="First Name", bgcolor=ft.colors.BLUE_100, color=ft.colors.BLACK)
    last_name_input = ft.TextField(
        label="Last Name", bgcolor=ft.colors.BLUE_100, color=ft.colors.BLACK)
    age_input = ft.TextField(
        label="Age", bgcolor=ft.colors.BLUE_100, color=ft.colors.BLACK)
    code_input = ft.TextField(
        label="Code", bgcolor=ft.colors.BLUE_100, color=ft.colors.BLACK)
    gender_dropdown = ft.Dropdown(
        label="Gender",
        options=[
            ft.dropdown.Option("Male"),
            ft.dropdown.Option("Female"),
            ft.dropdown.Option("Other"),
        ],
        bgcolor=ft.colors.BLUE_100,
        color=ft.colors.BLACK,
    )
    phone_input = ft.TextField(
        label="Phone", bgcolor=ft.colors.BLUE_100, color=ft.colors.BLACK)
    married_checkbox = ft.Checkbox(
        label="Married", fill_color=ft.colors.BLUE_100)
    add_visitor_button = ft.ElevatedButton(
        text="Add Visitor", on_click=add_visitor, bgcolor=ft.colors.BLUE_100, color=ft.colors.BLACK)

    input_tab = ft.Tab(
        text="Input",
        content=ft.Container(
            content=ft.Column(
                controls=[
                    first_name_input,
                    last_name_input,
                    age_input,
                    code_input,
                    gender_dropdown,
                    phone_input,
                    married_checkbox,
                    add_visitor_button,
                ],
                spacing=10,
            ),
            padding=20,
            bgcolor=ft.colors.BLUE_900,  
        ),
    )

    last_name_reservation_dropdown = ft.Dropdown(
        label="Select Last Name",
        options=[],
        bgcolor=ft.colors.GREEN_100,
        color=ft.colors.BLACK,
    )
    year_dropdown = ft.Dropdown(
        label="Year",
        options=[ft.dropdown.Option(str(year)) for year in range(1400, 1410)],
        bgcolor=ft.colors.GREEN_100,
        color=ft.colors.BLACK,
    )
    month_dropdown = ft.Dropdown(
        label="Month",
        options=[ft.dropdown.Option(str(month).zfill(2))
                 for month in range(1, 13)],
        bgcolor=ft.colors.GREEN_100,
        color=ft.colors.BLACK,
    )
    day_dropdown = ft.Dropdown(
        label="Day",
        options=[ft.dropdown.Option(str(day).zfill(2))
                 for day in range(1, 32)],
        bgcolor=ft.colors.GREEN_100,
        color=ft.colors.BLACK,
    )
    hour_dropdown = ft.Dropdown(
        label="Hour",
        options=[ft.dropdown.Option(str(hour).zfill(2))
                 for hour in range(0, 24)],
        bgcolor=ft.colors.GREEN_100,
        color=ft.colors.BLACK,
    )
    minute_dropdown = ft.Dropdown(
        label="Minute",
        options=[ft.dropdown.Option(str(minute).zfill(2))
                 for minute in range(0, 60, 5)],
        bgcolor=ft.colors.GREEN_100,
        color=ft.colors.BLACK,
    )
    make_reservation_button = ft.ElevatedButton(
        text="Make Reservation", on_click=make_reservation, bgcolor=ft.colors.GREEN_100, color=ft.colors.BLACK)

    reservation_tab = ft.Tab(
        text="Reservation",
        content=ft.Container(
            content=ft.Column(
                controls=[
                    last_name_reservation_dropdown,
                    ft.Row([year_dropdown, month_dropdown,
                           day_dropdown], spacing=10),
                    ft.Row([hour_dropdown, minute_dropdown], spacing=10),
                    make_reservation_button,
                ],
                spacing=10,
            ),
            padding=20,
            bgcolor=ft.colors.GREEN_900,  # Dark green background
        ),
    )

    visitor_list = ft.ListView(expand=True)

    visitor_list_tab = ft.Tab(
        text="Visitor List",
        content=ft.Container(
            content=ft.Column(
                controls=[
                    visitor_list,
                ],
            ),
            padding=20,
            bgcolor=ft.colors.RED_900, 
        ),
    )

    def update_last_name_dropdown():
        last_name_reservation_dropdown.options = [
            ft.dropdown.Option(visitor.last_name) for visitor in visitors
        ]
        page.update()

    def on_tab_change(e):
        if e.control.selected_index == 1:  # Reservation tab
            update_last_name_dropdown()
        elif e.control.selected_index == 2:  # Visitor List tab
            update_visitor_list()

    tabs = ft.Tabs(
        selected_index=0,
        on_change=on_tab_change,
        tabs=[input_tab, reservation_tab, visitor_list_tab],
    )

    page.add(tabs)


ft.app(target=main)
