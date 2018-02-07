//
//  StringCommandLineColorExtension.swift
//  HelloQuantum
//
//  Created by boland on 12/14/17.
//  Copyright © 2017 James Wootton. All rights reserved.
//

import Foundation

extension String {
    
    var redColor: String {
        return addColor(code: "31")
    }
    
    var blueColor: String {
        return addColor(code: "34")
    }
    
    var purpleColor: String {
        return addColor(code: "35")
    }
    
    var whiteColor: String {
        return addColor(code: "37")
    }
    
    func addColor(code: String) -> String {
        return "\u{001B}[0;" + code + "m" + self + "\u{001B}[0m"
    }
}
