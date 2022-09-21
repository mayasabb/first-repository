import Consts
import pygame
import os

question_window_Name = pygame.display.set_caption("question")
WINDOW = pygame.display.set_mode(
        (Consts.QUESTION_SCREEN_WIDTH, Consts.QUESTION_SCREEN_LENGTH))

# GAME_WINDOW = pygame.display.set_mode((Consts.GAME_WINDOW_WIDTH, Consts.GAME_WINDOW_LENGTH))

# def picture(i):
#     QUESTION_PICTURE = pygame.image.load(os.path.join(Consts.QUESTIONS_DICT["question"][i]))
#     PICTURE_WIDTH = Consts.QUESTION_SCREEN_WIDTH
#     PICTURE_HEIGHT = Consts.QUESTION_SCREEN_LENGTH
#     QUESTION_PICTURE_RESIZE = pygame.transform.scale(QUESTION_PICTURE, (PICTURE_WIDTH, PICTURE_HEIGHT))
#     WINDOW.blit(QUESTION_PICTURE_RESIZE, (325, 112.5))
#     pygame.display.update()

answers_keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4 ]


def open_questions_window():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # GAME_WINDOW.fill(Consts.GAME_WINDOW_COLOR)
            if event.type == pygame.KEYDOWN:
                for i in range(len(Consts.QUESTIONS_DICT["question"])):
                    if event.key == pygame.K_RETURN:
                        QUESTION_PICTURE = pygame.image.load(os.path.join('question1.png'))
                        PICTURE_WIDTH = Consts.QUESTION_SCREEN_WIDTH
                        PICTURE_HEIGHT = Consts.QUESTION_SCREEN_LENGTH
                        QUESTION_PICTURE_RESIZE = pygame.transform.scale(QUESTION_PICTURE, (PICTURE_WIDTH, PICTURE_HEIGHT))
                        WINDOW.blit(QUESTION_PICTURE_RESIZE, (0, 0))
                        # for j in range(len(answers_keys)):
                        if event.type == pygame.KEYDOWN:
                            if event.key in answers_keys:
                                if event.key == Consts.QUESTIONS_DICT["answers"][i]:
                                    break

                        pygame.display.update()

                        # pygame.time.delay(3000)
    pygame.quit()


if __name__ == "__Screen__":
    open_questions_window()

open_questions_window()