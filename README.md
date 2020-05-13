# chess-pi-game-quality

When pressing a button you get the status of blunders/excellent moves made during last game.

## Steps

- fetch latest game from [lichess](https://lichess.org/)
- local evaluation game using `pychess`
- `gpiozero` code to light leds/connect button