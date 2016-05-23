import os
from io import StringIO
from os.path import abspath, dirname, isfile

import pytest
from django.core.management import call_command
from django.core.management.base import CommandError

FLOW_PATH = 'tests.testapp.flows.TestFlow'


def test_create_graph():
    stdout = StringIO()
    call_command('flow_graph', "{}".format(FLOW_PATH), stdout=stdout)
    stdout.seek(0)
    graph = stdout.read()
    assert 'start -> savable_task' in graph
    assert 'savable_task -> if_task' in graph
    assert 'if_task -> switch_task' in graph
    assert 'switch_task -> end' in graph


def test_create_graph_svg():
    call_command('flow_graph', "{}".format(FLOW_PATH), svg=True)
    source_file_name = "{}".format(FLOW_PATH)
    svg_file_name = "{}.svg".format(FLOW_PATH)
    source_file_path = os.path.join(dirname(dirname(abspath(__file__))), source_file_name)
    svg_file_path = os.path.join(dirname(dirname(abspath(__file__))), svg_file_name)
    try:
        assert isfile(source_file_path)
        assert isfile(svg_file_path)
        with open(source_file_path, 'r') as f:
            f.seek(0)
            graph = f.read()
            assert 'start -> savable_task' in graph
            assert 'savable_task -> if_task' in graph
            assert 'if_task -> switch_task' in graph
            assert 'switch_task -> end' in graph
    finally:
        os.remove(source_file_path)
        os.remove(svg_file_path)


def test_create_graph_wrong_name():
    """Test exceptions"""
    with pytest.raises(CommandError):
        call_command('flow_graph', "wrong_path.TestFlow")

    with pytest.raises(CommandError):
        call_command('flow_graph', "wrong_path")

    with pytest.raises(CommandError):
        call_command('flow_graph', "tests.testapp.flows.WrongFlow")

    with pytest.raises(CommandError):
        call_command('flow_graph', "wrong_path")
