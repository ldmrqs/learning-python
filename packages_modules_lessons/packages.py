# packages contain multiple modules
import sample_packages.sample_module as sm
sm.hello()

#example2
from sample_packages import sample_module, sample_module2
sample_module.hello()
sample_module2.hello()