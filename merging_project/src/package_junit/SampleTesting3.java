package package_junit;

import static org.junit.Assert.assertEquals;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class SampleTesting3 {

	@Test
	void testDivision() {
        SampleTesting s = new SampleTesting();
		
		assertEquals(2,s.division(5, 2));
		fail("Not yet implemented");
		
	}

}
