from .models import Estudiante, Profesor, Curso, Direccion

def crear_curso(codigo, nombre, version):
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, version=version)
    return curso

def crear_profesor(rut, nombre):
    profesor = Profesor.objects.create(rut=rut, nombre=nombre)
    return profesor

def crear_estudiante(rut, nombre, apellido, fecha_nac, activo, creado_por):
    estudiante = Estudiante.objects.create(rut=rut, nombre=nombre, apellido=apellido,
                                           fecha_nac=fecha_nac, activo=activo,
                                           creado_por=creado_por)
    return estudiante

def crear_direccion(estudiante_id, calle, numero, comuna, ciudad, region, dpto=None):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    direccion = Direccion.objects.create(estudiante=estudiante, calle=calle, numero=numero,
                                         dpto=dpto, comuna=comuna, ciudad=ciudad, region=region)
    return direccion

def obtiene_estudiante(rut):
    estudiante = Estudiante.objects.get(rut=rut)
    return estudiante

def obtiene_profesor(rut):
    profesor = Profesor.objects.get(rut=rut)
    return profesor

def obtiene_curso(codigo):
    curso = Curso.objects.get(codigo=codigo)
    return curso

def agrega_profesor_a_curso(codigo_curso, rut_profesor):
    curso = Curso.objects.get(codigo=codigo_curso)
    profesor = Profesor.objects.get(rut=rut_profesor)
    curso.profesor = profesor
    curso.save()

def agrega_cursos_a_estudiante(rut_estudiante, codigos_cursos):
    estudiante = Estudiante.objects.get(rut=rut_estudiante)
    cursos = Curso.objects.filter(codigo__in=codigos_cursos)
    estudiante.cursos.add(*cursos)

def imprime_estudiante_cursos(rut_estudiante):
    estudiante = Estudiante.objects.get(rut=rut_estudiante)
    cursos_estudiante = estudiante.cursos.all()
    cursos_info = []
    for curso in cursos_estudiante:
        cursos_info.append({
            'codigo': curso.codigo,
            'nombre': curso.nombre,
            'version': curso.version
        })
    return cursos_info
