#!/usr/bin/env python3
import brain_games.games.even
import brain_games.engine


def main():
    name = brain_games.engine.greeting()
    brain_games.engine.action(name)


if __name__ == '__main__':
    main()
