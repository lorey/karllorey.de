---
id: 1458
title: Annotations in Java
date: 2013-02-05T21:42:53+00:00
author: Karl Lorey
layout: page
guid: http://www.karllorey.de/?page_id=1458
---
## Definition der Annotation

<pre class="brush: java; title: ; notranslate" title="">package aufgabe13;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Retention(RetentionPolicy.RUNTIME)
public @interface Student {
    String name();

    int matrikel();
}

</pre>

## Nutzung der Annotation

<pre class="brush: java; title: ; notranslate" title="">package aufgabe13;

/**
 *
 * @author Karl Lorey
 *
 */
@Student(name = "Peter Müller", matrikel = 3141592)
public class Application {
    public static void main(String[] args) {
        if (hasStudentAnnotation(Application.class)) {
            printStudentAnnotation(Application.class);
        }
    }

    private static boolean hasStudentAnnotation(Class&lt;?&gt; c) {
        return c.isAnnotationPresent(Student.class);
    }

    private static void printStudentAnnotation(Class&lt;?&gt; c) {
        Student s = c.getAnnotation(Student.class);
        System.out.println("Student Information:");
        System.out.println("- Name:     " + s.name());
        System.out.println("- Matrikel: " + s.matrikel());
    }
}
</pre>