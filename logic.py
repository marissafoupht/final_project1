from PyQt6.QtWidgets import *
from main_menu_gui import *


class Logic(QMainWindow, Ui_main_menu):
    """
    'Logic' class is the controller class for project. All changeable and new code is place inside.
    imports PyQt6 widgets and main_menu_gui
    """
    def __init__(self) -> None:
        """
        Initializes Logic class and sets up UI.

        Sets current window page to home.page.

        Displays candidates page when button_display_candidates is clicked.
        Displays voting page when button_vote is clicked.

        donald_trump_count = vote count for Donald Trump
        ted_cruz_count = vote count for Ted Cruz
        hillary_clinton_count = vote count for Hillary Clinton
        bernie_sanders_count = vote count for Bernie Sanders
        total_votes = total of all candidates votes

        :param: = none
        :returns: = none
        """
        super().__init__()
        self.setupUi(self)

        self.stackedWidget.setCurrentWidget(self.home_page)

        self.button_display_candidates.clicked.connect(lambda: self.show_candidates_page())
        self.button_vote.clicked.connect(lambda: self.show_vote_page())

        self.donald_trump_count = 0
        self.ted_cruz_count = 0
        self.hillary_clinton_count = 0
        self.bernie_sanders_count = 0
        self.total_votes = 0

    def show_candidates_page(self) -> None:
        """
        Method erases candidate current standings and displays available candidate choices.

        :param: = none
        :return: = none
        """
        self.label_current_standings.setText(f'')
        self.stackedWidget.setCurrentWidget(self.display_candidates_page)

    def show_vote_page(self) -> None:
        """
        Method erases candidate current standings and displays voting page where users choose
        the party they would like to vote for.

        If button_republican is clicked, show_republican_choice_page is called
        If button_democratic is clicked, show_democratic_choice_page is called

        :param: = none
        :return: = none
        """
        self.label_current_standings.setText(f'')
        self.stackedWidget.setCurrentWidget(self.party_choice_page)
        self.button_republican.clicked.connect(lambda: self.show_republican_choice_page())
        self.button_democratic.clicked.connect(lambda: self.show_democratic_choice_page())

    def show_republican_choice_page(self) -> None:
        """
        Method displays republican candidate choices, then calls check_repub_radios method
        to check radio button activity when button_submit_repub is clicked.

        :param: = none
        :return: = none
        """
        self.stackedWidget.setCurrentWidget(self.candidate_choice_republican_page)
        self.button_submit_repub.clicked.connect(lambda: self.check_repub_radios())

    def show_democratic_choice_page(self) -> None:
        """
        Method displays democratic candidate choices, then calls check_demo_radios method
        to check radio button activity when button_submit_deno is clicked.

        :param: = none
        :return: = none
        """
        self.stackedWidget.setCurrentWidget(self.candidate_choice_democratic_page)
        self.button_submit_demo.clicked.connect(lambda: self.check_demo_radios())

    def check_repub_radios(self) -> None:
        """
        Method checks user interaction with republican candidate radio buttons.
        If no button selected, returns text message prompting user.
        If Donald Trump radio button checked, Donald Trump vote count plus 1
        If Ted Cruz  radio button checked, Ted Cruz vote count plus 1

        :param: = none
        :return: = none
        """
        if self.radiobutton_donald_vote.isChecked() is False and self.radiobutton_ted_vote.isChecked() is False:
            self.label_repub_exceptions.setText(f'Must choose a candidate first.')
            self.button_submit_repub.clicked.connect(lambda: self.check_repub_radios())
        elif self.radiobutton_donald_vote.isChecked():
            self.donald_trump_count += 1
            self.stackedWidget.setCurrentWidget(self.home_page)
            self.current_standings()
        else:
            self.ted_cruz_count += 1
            self.stackedWidget.setCurrentWidget(self.home_page)
            self.current_standings()

    def check_demo_radios(self) -> None:
        """
        Method checks user interaction with democratic candidate radio buttons.
        If no button selected, returns text message prompting user.
        If Hillary Clinton radio button checked, Hillary Clinton vote count plus 1
        If Bernie Sanders radio button checked, Bernie Sanders vote count plus 1

        :param: = none
        :return: = none
        """
        if self.radiobutton_hillary_vote.isChecked() is False and self.radiobutton_bernie_vote.isChecked() is False:
            self.label_demo_exceptions.setText(f'Must choose a candidate first.')
            self.button_submit_demo.clicked.connect(lambda: self.check_demo_radios())
        elif self.radiobutton_hillary_vote.isChecked():
            self.hillary_clinton_count += 1
            self.stackedWidget.setCurrentWidget(self.home_page)
            self.current_standings()
        else:
            self.bernie_sanders_count += 1
            self.stackedWidget.setCurrentWidget(self.home_page)
            self.current_standings()

    def current_standings(self) -> None:
        """
        Method adds all counts together into a total_votes count.
        Sets label_current_standings on current page to text listing candidates and number of
        votes, along with the total number of votes.

        :param: = none
        :return: = none
        """
        self.total_votes = self.donald_trump_count + self.ted_cruz_count + self.hillary_clinton_count + self.bernie_sanders_count
        self.label_current_standings.setText(f"Current Polls: Trump = {self.donald_trump_count}, Cruz = {self.ted_cruz_count}, Clinton = {self.hillary_clinton_count}, Sanders = {self.bernie_sanders_count}, Total Votes = {self.total_votes}")
