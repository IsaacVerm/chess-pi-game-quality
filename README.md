# chess-pi-game-quality

When pressing a button you get the status of blunders/excellent moves made during last game.

## Setup

Setup Python environment:

```
python3 -m venv venv;
source venv/bin/activate;
pip install -r requirements.txt
```

To evaluate the games locally Stockfish is required. Installing Stockfish is different depending on your processor. In any case you have to make sure the `stockfish_path` variable at the top of `game_quality.py` points to this binary. 

### Install Stockfish on Mac

The engine binary can be downloaded [here](https://stockfishchess.org/download/). The binary you need is `stockfish-11-64` which can be found in the `/Mac` folder. 

### Install Stockfish on Raspberry

Install Stockfish on the Raspberry itself by running:

```
sudo apt-get update;
sudo apt-get install;
```

Stockfish is installed at `/usr/games/stockfish`. You can [verify this yourself](https://askubuntu.com/questions/129022/determine-destination-location-of-apt-get-install-package).

## Steps

- fetch latest game from [Lichess](https://lichess.org/) with [requests](https://requests.readthedocs.io/en/master/)
- local evaluation game using [python-chess](https://github.com/niklasf/python-chess)
- [gpiozero](https://github.com/gpiozero/gpiozero) code to light leds/connect button

## Fetch latest game

There's a dedicated library for more easily using the [Lichess API in Python](https://github.com/cyanfish/python-lichess) but it seems poorly maintained. I prefer to use `requests`. Although a bit more upfront work, it's easier to maintain over the long term.

I'm in luck because the Lichess API already provides an endpoint which does exactly what I need. The [/api/user/{username}/current-game](https://lichess.org/api#operation/apiUserCurrentGame) downloads the ongoing game, OR (my situation) the last game played of a user. Even better, no authorization is required to fetch this game.

`python-chess`, the library used to evaluate moves later on, [only accepts pgn](https://python-chess.readthedocs.io/en/latest/pgn.html). 

## Local evaluation game

Evaluation is done using Stockfish. Based on the score in [centipawns](https://lichess.org/faq#acpl) Lichess determines if a move is an inaccuracy, mistake or blunder. Note: the best move loses 0 centipawns, it's not possible to gain centipawns by making a good move.

Based on the score I determine if a move is a blunder or a great move. There are some [posts](https://lichess.org/forum/general-chess-discussion/what-exactly-is-a-innac--mistake--blunder) about the exact evaluations. I consider it a great move if I lose less than 10 centipawns and a blunder when losing more than 200 centipawns.

## Iot

