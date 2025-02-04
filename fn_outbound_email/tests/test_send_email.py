# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_outbound_email"
FUNCTION_NAME = "send_email"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_send_email_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("send_email", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("send_email_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestSendEmail:
    """ Tests for the send_email function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.livetest #can be removed in future when attachment mock endpoint is updated
    @pytest.mark.parametrize("mail_from, mail_incident_id, mail_to, mail_cc, mail_bcc, mail_subject, mail_body_text", [
        ("a@example.com", 123, "b@example.com", "c@example.com", "d@example.com", "text", "text"),
        ("a@example.com", 123, "b@example.com", "c@example.com", "d@example.com", "text", "text")
    ])
    def test_success(self, circuits_app, mail_from, mail_incident_id, mail_to, mail_cc, mail_bcc, mail_subject, mail_body_text):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "mail_from": mail_from,
            "mail_incident_id": mail_incident_id,
            "mail_to": mail_to,
            "mail_cc": mail_cc,
            "mail_bcc": mail_bcc,
            "mail_subject": mail_subject,
            "mail_body_text": mail_body_text
        }
        results = call_send_email_function(circuits_app, function_params)
        assert(results['success'])
