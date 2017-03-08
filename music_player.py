import os
import sys

import pygame as pg
import pygame.mixer as music
from guipack import movewindow, scrollwindow
from guipack.subrect import Subrect
from analysis import analyze_audio
# def music_selector(song_name):

song_dict = {
    'Daughter': './music_files/daughter.wav',
    'It Aint Me': './music_files/selenagomez.wav'
}


def play_selected_song(selected_song):
    song = pg.mixer.music.load(song_dict.get(selected_song))
    pg.mixer.music.play(0, 0.0)


def gen_song_names():
    """Just getting sample content from a dict."""
    song_names = []
    for song_name in song_dict:
        song_names.append(song_name)
    return song_names


class MusicPlayerWindow(object):
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.done = False
        self.clock = pg.time.Clock()
        self.fps = 60
        self.win = self.make_win()
        self.selected_song_name = ''
        self.already_ran = False

    def make_visulization(self, song_name, x, y):
        self.selected_song_name = song_name
        myfont = pg.font.SysFont("monospace", 15)
        label = myfont.render(str(self.selected_song_name), 1, (255,255,0))
        text = self.screen.blit(label, (x, y))
        self.already_ran = True
        pg.display.update()


    def make_win(self):
        myfont = pg.font.SysFont("monospace", 15)
        """Setup a movable window that contains a scroll window."""
        window_args = {"text": "Songs You Can Play",
                       "font": FONT,
                       "text_color": (255, 255, 255)}
        win = movewindow.MoveWindow(Subrect((50, 50, 200, 300)), **window_args)
        bar_subrect = Subrect((25, 45, 150, 230), win.subrect)
        bar = scrollwindow.ScrollWindow(
            bar_subrect, gen_song_names(), FONT)
        win.content.append(bar)
        return win

    def event_loop(self):
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                self.done = True
            get = self.win.get_events(event)
            if get:
                pg.display.set_caption(get)
                play_selected_song(get)
                self.make_visulization(get, 500, 500)
                song_data = analyze_audio(song_dict.get(get))
                self.make_visulization(song_data, 500, 600)
                pg.event.clear()
                return get



    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.screen.fill((25, 155, 255))
            self.win.update(self.screen)
            if not self.already_ran:
                self.make_visulization('No Song Selected', 500, 500 )
            self.clock.tick(self.fps)


if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    pg.display.set_caption("Music Player")
    pg.display.set_mode((1000, 1000))
    FONT = pg.font.SysFont("timesnewroman", 15)
    run_it = MusicPlayerWindow()
    run_it.main_loop()
    pg.quit()
    sys.exit()
