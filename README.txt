================================================================================

Compile Notes
-------------

To generate a compatible executable with the game interface, execute:
    pyinstaller --onefile main.py
    
The executable will be generated in dist/main/main

================================================================================

Runtime Notes
-------------

The command list as follows:

        name        - print the name of the Game Engine.
        print       - print the board.
        exit/quit   - quit the game.
        black XXXX  - place the black stone on the position XXXX in the board.
        white XXXX  - place the write stone on the XXXX in the board, X is the A-S.
        next        - the engine will search the move for next step.
        move XXXX   - tell the engine that the opponent take the move XXXX,
                        and the engine will search the move for next step.
        new black   - start a new game and set the engine to Black player.
        new white   - start a new game and set it to White.
        depth d     - set the alpha beta search depth, default is 6.
        help        - print this help.

