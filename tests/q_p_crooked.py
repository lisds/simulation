test = {
  'name': 'Question p_crooked',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_crooked'
          >>> 'p_crooked' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_crooked'
          >>> # from its initial state (of ...)
          >>> p_crooked is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          # n = 10000
          # rng = np.random.default_rng()
          # res = np.sum(rng.binomial(250, 0.5, (n, n)) >= 139, axis=1) / n
          # np.quantile(res, [0.001, 0.999])
          'code': r"""
          >>> 0.037 < p_crooked < 0.051
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}