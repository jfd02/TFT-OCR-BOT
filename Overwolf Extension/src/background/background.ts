import { OWWindow, OWGameListener, OWGames } from "@overwolf/overwolf-api-ts";
import RunningGameInfo = overwolf.games.RunningGameInfo;

class BackgroundController {
    private gameListener: OWGameListener;
    private overlay: OWWindow;

    constructor() {
        this.overlay = new OWWindow("overlay");

        this.gameListener = new OWGameListener({
            onGameStarted: this.toggleWindows.bind(this),
            onGameEnded: this.toggleWindows.bind(this)
        });
    };

    public async run() {
        this.gameListener.start();

        const gameIsRunning = await this.isTftRunning();

        if (gameIsRunning) {
            //overwolf.log.info("TFT running, overlay ready");
            this.overlay.restore();
        }
    }

    private toggleWindows(info) {
        if (!info || !this.isGameTft(info)) {
            return;
        }

        if (info.isRunning) {
            this.overlay.restore();
        } else {
            this.overlay.close();
        }
    }

    private async isTftRunning(): Promise<boolean> {
        const info = await OWGames.getRunningGameInfo();

        return info && info.isRunning && this.isGameTft(info);
    }

    private isGameTft(info: RunningGameInfo) {
        return info.classId === 5426;
    }
}

export const backgroundController = new BackgroundController();