package com.example.SpringBootForK8s.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@NoArgsConstructor  // will auto generate Default constructor
@AllArgsConstructor // Will generate all the parameterised constructor
@Data // Will generate getters and setters along with toString method
@Entity
@Table(name = "student")
public class Student {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int rollNo;
    private String name;
    private int marks;


}

