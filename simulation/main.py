"""
Entry point script
"""
if __package__ is None or __package__ == '':
    import simulation
else:
    from . import simulation


def main():
    """
    Entry point function
    :return:
    """
    simulator = simulation.Simulation()
    try:
        simulator.start()
    except KeyboardInterrupt:
        simulator.stop()


if __name__ == "__main__":
    main()
