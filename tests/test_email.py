from types import SimpleNamespace

from gtm_agent.gtm_agent import send_prospect_email


def test_send_prospect_email_blocks_disqualified_prospect():
    result = send_prospect_email.func(
        prospect={
            "prospect_id": "LEAD-50001",
            "name": "Priya Nair",
            "email": "priya.nair@brightwaveapps.com",
        },
        subject="Follow-up",
        body="Hello",
        runtime=SimpleNamespace(config={}),
    )

    assert result == {
        "status": "blocked",
        "error": "Prospect is marked disqualified; email not sent.",
    }


def test_send_prospect_email_sends_non_disqualified_prospect():
    result = send_prospect_email.func(
        prospect={
            "prospect_id": "LEAD-12853",
            "name": "Omar Okafor",
            "email": "omar.okafor@lakesideanalytics.com",
        },
        subject="Follow-up",
        body="Hello",
        runtime=SimpleNamespace(config={}),
    )

    assert result["status"] == "sent"
    assert result["to"] == "omar.okafor@lakesideanalytics.com"
