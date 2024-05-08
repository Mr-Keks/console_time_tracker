from ui.menu_navigation import main_menu_ui


if __name__ == '__main__':
    try:
        main_menu_ui()
    except KeyboardInterrupt:
        print("\nProgram has been closed by user...")