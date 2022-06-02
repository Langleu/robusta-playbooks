from robusta.api import *

@action
def pod_state(event: PodEvent):
    # we have full access to the pod on which the alert fired
    pod = event.get_pod
    if not pod:
        logging.error(
            f"cannot run PodState on alert with no pod object: {event}"
        )
        return

    # this is how you send data to slack or other destinations
    event.add_enrichment([
        MarkdownBlock("*Pod State* " + pod)
    ])
