import pygame
import sys
import main  # import your main.py

def login_page():
    pygame.init()

    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Login Page")

    # Load background image (YOUR FILE NAME)
    bg = pygame.image.load("background.jpeg")
    bg = pygame.transform.scale(bg, (800, 500))

    font_title = pygame.font.SysFont(None, 55)
    font_label = pygame.font.SysFont(None, 35)
    font_input = pygame.font.SysFont(None, 32)

    username = ""
    password = ""
    active_box = None   # Tracks which box is focused

    # Input fields & button
    input_rect_user = pygame.Rect(300, 180, 250, 40)
    input_rect_pass = pygame.Rect(300, 260, 250, 40)
    login_button = pygame.Rect(340, 340, 160, 50)

    while True:
        screen.blit(bg, (0, 0))

        # Title
        title = font_title.render("Login to EmotionBeat", True, (255, 255, 255))
        screen.blit(title, (220, 80))

        # Labels
        screen.blit(font_label.render("Username:", True, (255, 255, 255)), (160, 185))
        screen.blit(font_label.render("Password:", True, (255, 255, 255)), (160, 265))

        # Input boxes
        pygame.draw.rect(screen, (0, 0, 0), input_rect_user, border_radius=8)
        pygame.draw.rect(screen, (0, 0, 0), input_rect_pass, border_radius=8)

        # Show text
        screen.blit(font_input.render(username, True, (255, 255, 255)),
                    (input_rect_user.x + 10, input_rect_user.y + 8))

        screen.blit(font_input.render("*" * len(password), True, (255, 255, 255)),
                    (input_rect_pass.x + 10, input_rect_pass.y + 8))

        # Login button
        pygame.draw.rect(screen, (50, 50, 50), login_button, border_radius=8)
        screen.blit(font_label.render("Login", True, (255, 255, 255)),
                    (login_button.x + 45, login_button.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Click detection
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect_user.collidepoint(event.pos):
                    active_box = "user"
                elif input_rect_pass.collidepoint(event.pos):
                    active_box = "pass"
                elif login_button.collidepoint(event.pos):
                    if username == "admin" and password == "1234":
                        pygame.quit()
                        main.main()  # Go to main page
                    else:
                        print("Invalid Login!")
                else:
                    active_box = None

            # Keyboard typing
            if event.type == pygame.KEYDOWN:
                if active_box == "user":
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode

                if active_box == "pass":
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

        pygame.display.update()


if __name__ == "__main__":
    login_page()
