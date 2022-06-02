from robusta.api import *
from hikaru import get_clean_dict
import json

@action
def pod_state(event: PodEvent):
    # we have full access to the pod on which the alert fired
    pod = event.get_pod()
    if not pod:
        logging.error(
            f"cannot run PodState on alert with no pod object: {event}"
        )
        return

    oom = False
    pod_dict = get_clean_dict(pod)
    if "OOMKilled" in json.dumps(pod_dict):
        oom = True

    # this is how you send data to slack or other destinations
    event.add_enrichment([
        MarkdownBlock("*Pod State* " + pod.status.phase),
        MarkdownBlock("*Previously OOM killed? * " + str(oom))
    ])
