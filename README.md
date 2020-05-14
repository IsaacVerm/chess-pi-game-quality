# chess-pi-game-quality

When pressing a button you get the status of blunders/excellent moves made during last game.

## Setup

Setup Python environment:

```
python3 -m venv venv;
source venv/bin/activate;
pip install -r requirements.txt
```

To evaluate the games locally Stockfish is required. The engine binary can be downloaded [here](https://stockfishchess.org/download/). The binary you need is `stockfish-11-64` which can be found in the `/Mac` folder. Make sure `evaluate-games.py` points to this binary. 

## Steps

- fetch latest game from [Lichess](https://lichess.org/) with [requests](https://requests.readthedocs.io/en/master/)
- local evaluation game using [python-chess](https://github.com/niklasf/python-chess)
- [gpiozero](https://github.com/gpiozero/gpiozero) code to light leds/connect button

## Fetch latest game

There's a dedicated library for more easily using the [Lichess API in Python](https://github.com/cyanfish/python-lichess) but it seems poorly maintained. I prefer to use `requests`. Although a bit more upfront work, it's easier to maintain over the long term.

I'm in luck because the Lichess API already provides an endpoint which does exactly what I need. The [/api/user/{username}/current-game](https://lichess.org/api#operation/apiUserCurrentGame) downloads the ongoing game, OR (my situation) the last game played of a user. Even better, no authorization is required to fetch this game.

`python-chess`, the library used to evaluate moves later on, [only accepts pgn](https://python-chess.readthedocs.io/en/latest/pgn.html). 

## Local evaluation game