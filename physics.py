"""
Basic Physics Formula Library
-----------------------------
Five commonly used physics formulas, with SI units noted.
"""

def speed(distance_m, time_s):
    """Calculate speed: v = d / t (m/s)."""
    if time_s == 0:
        raise ValueError("Time cannot be zero.")
    return distance_m / time_s


def force(mass_kg, acceleration_m_s2):
    """Calculate force: F = m * a (newtons)."""
    return mass_kg * acceleration_m_s2


def kinetic_energy(mass_kg, velocity_m_s):
    """Calculate kinetic energy: KE = 1/2 * m * v^2 (joules)."""
    return 0.5 * mass_kg * velocity_m_s ** 2


def potential_energy(mass_kg, gravity_m_s2, height_m):
    """Calculate gravitational potential energy: PE = m * g * h (joules)."""
    return mass_kg * gravity_m_s2 * height_m


def density(mass_kg, volume_m3):
    """Calculate density: rho = m / V (kg/m^3)."""
    if volume_m3 == 0:
        raise ValueError("Volume cannot be zero.")
    return mass_kg / volume_m3


if __name__ == "__main__":
    print("Physics Formula Examples")
    print("------------------------")
    print(f"Speed: {speed(100, 20):.2f} m/s")
    print(f"Force: {force(5, 3):.2f} N")
    print(f"Kinetic energy: {kinetic_energy(2, 4):.2f} J")
    print(f"Potential energy: {potential_energy(2, 9.81, 5):.2f} J")
    print(f"Density: {density(10, 2):.2f} kg/m^3")
