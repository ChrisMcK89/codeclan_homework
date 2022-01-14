import unittest

from src.guests import *
from src.rooms import *
from src.songs import *

class TestCaraoke(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Chris", 10)
        self.guest2 = Guest("Rory", 15)
        self.guest3 = Guest("Callum", 20)

        self.song1 = Song("Queen", "Don't stop me now" )
        self.song2 = Song("Coldplay", "Yellow")
        self.song3 = Song("U2", "Vertigo")

        self.room1 = Room("Room1")
        self.room2 = Room("Room2")
        self.room3 = Room("Room3")
        self.room4 = Room("Room4")

    def test_song_has_artist(self):
        self.assertEqual("Queen", self.song1.artist)

    def test_song_has_title(self):
        self.assertEqual("Yellow", self.song2.title)

    def test_guest_has_name(self):
        self.assertEqual("Chris", self.guest1.name)

    def test_room_has_name(self):
        self.assertEqual("Room1", self.room1.room_name)

    def test_add_guest(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        self.assertEqual(2, len(self.room1.guests))

    def test_add_song(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, len(self.room1.songs))

    def test_remove_guest(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        self.room1.add_guest(self.guest3)
        self.room1.remove_guest(self.guest1)
        self.assertEqual(2, len(self.room1.guests))

    def test_room_is_full(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        self.room1.add_guest(self.guest3)
        self.assertEqual("room full", self.room1.room_is_full())
    
    def test_check_guest_wallet(self):
        self.assertEqual(10, self.guest1.check_wallet())

    def test_room_fee(self):
        self.assertEqual(5, self.room1.fee)

    def test_reduce_wallet_by_fee(self):
        self.room1.add_guest(self.guest1)
        self.guest1.reduce_wallet_by_fee(self.room1.fee)
        self.assertEqual(5, self.guest1.check_wallet())

    
