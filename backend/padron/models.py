from django.db import models

class Vivienda(models.Model):
    numero = models.CharField(max_length=50, unique=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    pisos = models.IntegerField(blank=True, null=True)
    calle = models.CharField(max_length=100, blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)
    parqueo_num = models.CharField(max_length=50, blank=True, null=True)
    area_m2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return f"Vivienda {self.numero}"

class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    documento_tipo = models.CharField(max_length=30, blank=True, null=True)
    documento_numero = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return f"{self.apellidos}, {self.nombres}"

class PersonaVivienda(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="vinculos_vivienda")
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE, related_name="vinculos_persona")
    rol_en_vivienda = models.CharField(max_length=50, blank=True, null=True)
    fecha_desde = models.DateField(blank=True, null=True)
    fecha_hasta = models.DateField(blank=True, null=True)
    es_responsable = models.BooleanField(default=False)
    class Meta:
        unique_together = ("persona", "vivienda")
    def __str__(self): return f"{self.persona} ↔ {self.vivienda} ({self.rol_en_vivienda or '-'})"

class Vehiculo(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True, related_name="vehiculos")
    vivienda = models.ForeignKey(Vivienda, on_delete=models.SET_NULL, null=True, blank=True, related_name="vehiculos")
    placa = models.CharField(max_length=20, unique=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    activo = models.BooleanField(default=True)
    def __str__(self): return self.placa

class Mascota(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True, related_name="mascotas")
    vivienda = models.ForeignKey(Vivienda, on_delete=models.SET_NULL, null=True, blank=True, related_name="mascotas")
    nombre = models.CharField(max_length=80)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    raza = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    def __str__(self): return self.nombre
