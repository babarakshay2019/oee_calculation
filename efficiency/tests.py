from datetime import datetime, timedelta
from django.test import TestCase
from django.utils.timezone import make_aware
from efficiency.models import Machine, ProductionLog
from efficiency.utils import calculate_oee

class MachineModelTestCase(TestCase):
    
    def setUp(self):
        """Set up initial data for testing."""
        self.machine = Machine.objects.create(
            machine_name='Machine 1',
            machine_serial_no='ABC123'
        )
        
        current_time = make_aware(datetime.now().replace(microsecond=0))
        duration = timedelta(minutes=5)
        self.production_log = ProductionLog.objects.create(
            cycle_no='CN001',
            unique_id='UID001',
            material_name='Material 1',
            machine=self.machine,
            start_time=current_time,
            end_time=current_time + duration,
            duration=duration
        )
    
    def test_machine_creation(self):
        """Test Machine model creation."""
        self.assertEqual(self.machine.machine_name, 'Machine 1')
        self.assertEqual(self.machine.machine_serial_no, 'ABC123')
    
    def test_machine_str_method(self):
        """Test __str__ method of Machine model."""
        self.assertEqual(str(self.machine), 'Machine 1')
    
    def test_get_machine_list(self):
        """Test getting list of machines."""
        machines = Machine.objects.all()
        self.assertEqual(len(machines), 1)
        self.assertEqual(machines[0], self.machine)
    
    def test_get_production_log_list(self):
        """Test getting list of production logs."""
        production_logs = ProductionLog.objects.all()
        self.assertEqual(len(production_logs), 1)
        self.assertEqual(production_logs[0], self.production_log)
    
    def test_create_production_log(self):
        """Test creating production log."""
        current_time = make_aware(datetime.now().replace(microsecond=0))
        duration = timedelta(minutes=5)
        production_log = ProductionLog.objects.create(
            cycle_no='CN002',
            unique_id='UID002',
            material_name='Material 2',
            machine=self.machine,
            start_time=current_time,
            end_time=current_time + duration,
            duration=duration
        )
        self.assertEqual(production_log.cycle_no, 'CN002')
    
    def test_oee_view(self):
        """Test OEE calculation."""
        oee, availability, performance, quality = calculate_oee(self.production_log)
        self.assertAlmostEqual(oee, 3472.222222222222, places=3)
        self.assertAlmostEqual(availability, 0.3472222222222222, places=3)
        self.assertEqual(performance, 100)
        self.assertEqual(quality, 100)
