#!/usr/bin/env python3
import brain_games.games.prime
import brain_games.engine


def main():
    name = brain_games.engine.greeting()
    brain_games.engine.is_prime(name)


if __name__ == '__main__':
    main()
