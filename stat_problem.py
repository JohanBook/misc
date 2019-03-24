# -*- coding: utf-8 -*-
"""
stat_problem.py

Calculates conditional probability for repeated events from given selection in a moronic way.

Example:
 Calculate probability that given 3 children (events), and given that one is
 a boy (condition=boy), what is the probability they have a girl (target=girl)?
 >>> get_graph_probability({'girl': 1/2, 'boy': 1/2}, target='girl', condition='boy', num_events=4)
 0.9333333333333333
"""


def get_prob(dic, *keywords):
    """
    Sum probabilities for given keywords (all keywords must be found in probability name).

    Examples:
    >>> get_prob({'a': 0.2, 'b': 0.2, 'ab': 0.6}, 'ab')
    0.6
    >>> get_prob({'a': 0.2, 'b': 0.2, 'ab': 0.6}, 'a')
    0.8
    >>> get_prob({'a': 0.2, 'b': 0.2, 'ab': 0.6}, '')
    1.0
    >>> get_prob({'a': 0.2, 'b': 0.2, 'ab': 0.6})
    1.0
    >>> get_prob({'blue_car': 0.2, 'red_car': 0.2, 'blue_truck': 0.6}, 'blue', 'car')
    0.2
    """
    assert dic is not None, 'Given dict cannot be None'
    return sum([v if all(kw in k for kw in keywords) else 0 for k, v in dic.items()])


def create_event_graph(categories, num_events):
    """
    Create layer for probability tree given possible events (categories) and number of events (steps)

    >>> create_event_graph({'a': 1/2, 'b': 1/2}, num_events=1)
    {'a': 0.5, 'b': 0.5}

    >>> create_event_graph({'a': 1/2, 'b': 1/2}, num_events=2)
    {'a-a': 0.25, 'a-b': 0.25, 'b-a': 0.25, 'b-b': 0.25}

    >>> create_event_graph({'a': 1/2, 'b': 1/2}, num_events=3)
    {'a-a-a': 0.125, 'a-a-b': 0.125, 'a-b-a': 0.125, 'a-b-b': 0.125, 'b-a-a': 0.125, 'b-a-b': 0.125, 'b-b-a': 0.125, 'b-b-b': 0.125}
    """

    def extend_graph(original_graph, extension):
        extended_graph = {}
        for e1 in original_graph.keys():
            for e2 in extension.keys():
                extended_graph[f'{e1}-{e2}'] = original_graph[e1] * extension[e2]
        return extended_graph

    total_event_prob = sum(categories.values())

    assert total_event_prob == 1, \
        f'Event probability does not sum to 1, got {total_event_prob}'

    event_graph = dict(categories)
    for _ in range(num_events-1):
        event_graph = extend_graph(event_graph, categories)

    total_event_prob = sum(event_graph.values())
    assert total_event_prob, \
        f'Produced event graph probability does not sum to 1, got {total_event_prob}'
    return event_graph


def get_graph_probability(categories, target, condition='', num_events=1):
    """
    Example
    >>> get_graph_probability({'girl': 1/2, 'boy': 1/2}, target='boy')
    0.5
    >>> get_graph_probability({'girl': 1/2, 'boy': 1/2}, target='girl', num_events=2)
    0.75
    >>> get_graph_probability({'girl': 1/2, 'boy': 1/2}, target='girl', condition='boy', num_events=2)
    0.6666666666666666
    """
    dual_events = create_event_graph(categories, num_events=num_events)
    return get_prob(dual_events, target, condition) / get_prob(dual_events, condition)


if __name__ == '__main__':
    events = {'f': 1/2, 'm_t': 1/14, 'm_nt': 3/7}
    for num_event in range(1, 5):
        print(num_event, ': P(f | m_t) =', get_graph_probability(events, target='f', condition='m_t', num_events=num_event))
