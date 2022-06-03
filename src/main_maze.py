from agent.agent_qtable import QTableAgent
from games.labyrinth.env_labyrinth import EnvLabyrinth
from games.labyrinth.labyrinth_game import LabyrinthGame
from monitoring.monitoring import PlotWriter


def run_qtable_agent(env):
    agent = QTableAgent(env)

    train_plot = PlotWriter("Training")
    train_plot.set_label("Epoche", "Reward")

    play_plot = PlotWriter("Play")
    play_plot.set_label("Epoche", "Reward")

    agent.register_writer_training(train_plot)
    agent.register_writer_play(play_plot)


    for i in range(0, 20):
        agent.train(50)
        agent.play(i)


def run_qnetwork_agent(env):
    from agent.agent_qnetwork import QNetworkAgent
    agent = QNetworkAgent(env)

    train_plot = PlotWriter("Training")
    train_plot.set_label("Epoche", "Reward")

    play_plot = PlotWriter("Play")
    play_plot.set_label("Epoche", "Reward")

    agent.register_writer_training(train_plot)
    agent.register_writer_play(play_plot)

    for i in range(0, 20):
        agent.train(50)
        agent.play(i)


print('--- Start ---')
env = EnvLabyrinth(LabyrinthGame.setup_game(6, 6, 5, 123))

#run_qtable_agent(env)
run_qnetwork_agent(env)

# Use this as a breakpoint to keep the plots open
print('--- END ---')
print("Input any key to exit...")
input()
